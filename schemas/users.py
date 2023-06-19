def user_serializer(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "email": user.get("email"),
        "phone_number": user.get("phone_number"),
        "password": user.get("password"),
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]