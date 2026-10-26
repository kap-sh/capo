"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationGrantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.grant


class GetApplicationGrantResponse(TypedDict, closed=True):
    grant: "capo_sso_admin.types.grant.Grant"
    """<p>A structure that describes the requested grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationGrantResponse) -> dict:
    out: dict = {}
    import capo_sso_admin.types.grant

    out["Grant"] = capo_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationGrantResponse:
    out: GetApplicationGrantResponse = {}  # type: ignore[typeddict-item]
    if data.get("Grant") is not None:
        import capo_sso_admin.types.grant

        out["grant"] = capo_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        out["grant"] = {"$unknown": {"name": ""}}
    return out
