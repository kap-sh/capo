"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ProspectingResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.prospecting_result_aws


class ProspectingResult(TypedDict, closed=True):
    aws: NotRequired[
        "capo_partnercentral_selling.types.prospecting_result_aws.ProspectingResultAws"
    ]
    """<p>Prospecting data and insights that AWS provides during the prospecting job. This includes customer details, task information, and scoring that AI generates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProspectingResult) -> dict:
    out: dict = {}
    if "aws" in value:
        import capo_partnercentral_selling.types.prospecting_result_aws

        out["Aws"] = (
            capo_partnercentral_selling.types.prospecting_result_aws.serialize_aws_json_1_0(
                value["aws"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProspectingResult:
    out: ProspectingResult = {}  # type: ignore[typeddict-item]
    if data.get("Aws") is not None:
        import capo_partnercentral_selling.types.prospecting_result_aws

        out["aws"] = (
            capo_partnercentral_selling.types.prospecting_result_aws.deserialize_aws_json_1_0(
                data["Aws"]
            )
        )
    return out


def redact_sensitive(value: ProspectingResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "aws" in value:
        import capo_partnercentral_selling.types.prospecting_result_aws

        out["aws"] = (
            capo_partnercentral_selling.types.prospecting_result_aws.redact_sensitive(
                value["aws"]
            )
        )
    return out
