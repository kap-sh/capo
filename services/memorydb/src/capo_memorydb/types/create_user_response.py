"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.user


class CreateUserResponse(TypedDict, closed=True):
    user: NotRequired["capo_memorydb.types.user.User"]
    """<p>The newly-created user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_memorydb.types.user

        out["User"] = capo_memorydb.types.user.serialize_aws_json_1_1(value["user"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_memorydb.types.user

        out["user"] = capo_memorydb.types.user.deserialize_aws_json_1_1(data["User"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_memorydb.types.user

        out["User"] = capo_memorydb.types.user.serialize_cbor(value["user"])
    return out


def deserialize_cbor(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("User") is not None:
        import capo_memorydb.types.user

        out["user"] = capo_memorydb.types.user.deserialize_cbor(data["User"])
    return out
