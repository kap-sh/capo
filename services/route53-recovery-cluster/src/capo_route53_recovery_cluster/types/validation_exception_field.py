"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.string


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_route53_recovery_cluster.types.string.String"
    """<p>The field that had the validation exception.</p>"""
    message: "capo_route53_recovery_cluster.types.string.String"
    """<p>Information about the validation exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
