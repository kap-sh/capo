"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PrincipalSearchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.principal_id
    import capo_cloudwatchomni.types.principal_type


class PrincipalSearchResult(TypedDict, closed=True):
    principal_id: "capo_cloudwatchomni.types.principal_id.PrincipalId"
    """The unique ID of the principal."""
    principal_type: "capo_cloudwatchomni.types.principal_type.PrincipalType"
    """Whether the principal is a user or a group."""
    display_name: "str"
    """The display name of the principal."""
    user_name: NotRequired["str"]
    """The user name of the principal. Present for users only."""
    description: NotRequired["str"]
    """An optional description of the principal."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrincipalSearchResult) -> dict:
    out: dict = {}
    out["principalId"] = value["principal_id"]
    import capo_cloudwatchomni.types.principal_type

    out["principalType"] = capo_cloudwatchomni.types.principal_type.serialize_cbor(
        value["principal_type"]
    )
    out["displayName"] = value["display_name"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> PrincipalSearchResult:
    out: PrincipalSearchResult = {}  # type: ignore[typeddict-item]
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    else:
        out["principal_id"] = ""
    if data.get("principalType") is not None:
        import capo_cloudwatchomni.types.principal_type

        out["principal_type"] = (
            capo_cloudwatchomni.types.principal_type.deserialize_cbor(
                data["principalType"]
            )
        )
    else:
        import typing

        out["principal_type"] = typing.cast(
            "capo_cloudwatchomni.types.principal_type.PrincipalType", ""
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
