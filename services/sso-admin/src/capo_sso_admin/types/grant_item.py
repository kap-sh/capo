"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GrantItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.grant
    import capo_sso_admin.types.grant_type


class GrantItem(TypedDict, closed=True):
    grant_type: "capo_sso_admin.types.grant_type.GrantType"
    """<p>The type of the selected grant.</p>"""
    grant: "capo_sso_admin.types.grant.Grant"
    """<p>The configuration structure for the selected grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantItem) -> dict:
    out: dict = {}
    import capo_sso_admin.types.grant_type

    out["GrantType"] = capo_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    import capo_sso_admin.types.grant

    out["Grant"] = capo_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GrantItem:
    out: GrantItem = {}  # type: ignore[typeddict-item]
    if data.get("GrantType") is not None:
        import capo_sso_admin.types.grant_type

        out["grant_type"] = capo_sso_admin.types.grant_type.deserialize_aws_json_1_1(
            data["GrantType"]
        )
    else:
        import typing

        out["grant_type"] = typing.cast("capo_sso_admin.types.grant_type.GrantType", "")
    if data.get("Grant") is not None:
        import capo_sso_admin.types.grant

        out["grant"] = capo_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        out["grant"] = {"$unknown": {"name": ""}}
    return out
