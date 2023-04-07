from konnector.sideb import (postgres_conn,
                             ReadOneTypedCursor)


from konnector.model import Owner, Response

from konnector.handler.session import is_session_alive, store_session_with_expiration


def __validate_user_input(form_data):
    with postgres_conn as conn:
        type = Owner
        stmt = f"SELECT {','.join(type.REQUIRED + type.OPTIONAL)} FROM owner WHERE email = %s AND password = %s"
        with ReadOneTypedCursor(connection=conn, stmt=stmt, type=type, params=[*form_data.values()]) as execute:
            result_set = execute
            return Owner.from_keys(**result_set)


def __auth_chain_builder(args=None, kwargs=None):
    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}
    return dict(
        pre=dict(),
        # pre=dict(
        #     ok=all,
        #     steps=[dict(name='User Session Alive',
        #          func=is_session_alive,
        #          inputs=args,
        #          return_type=Owner)
        #         ],
        # ),
        required=dict(
            ok=all,
            steps=[
                dict(name='Validate Input',
                     func=__validate_user_input,
                     inputs=args,
                     return_type=Owner
                     ),
                dict(name='Persist User Session',
                     func=store_session_with_expiration,
                     inputs=kwargs,
                     return_type=Owner
                     )
            ]
        ),
        post=dict()
    )


def start(form_data):
    auth_chain = __auth_chain_builder(args=[form_data])
    for group, nested in auth_chain.items():
        if nested:
            assertion = nested.get('ok')
            steps = nested.get('steps')
            result = None
            execution_result = []
            for step in steps:
                name, function, inputs, return_type, *_ = step.values()
                print(f'Executing: {name} -> function: {function} with input(s) **** and return type: {return_type}')
                if inputs:
                    result = function(*inputs)
                else:
                    result = function(result)
                execution_result.append(result)

            if assertion(execution_result):
                print(f'Last Step: {result}')
                return Response(200, message='OK', data=result)
    return Response(500, message='Something went wrong, :(')




