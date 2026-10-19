"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_list


class DescribeTrustedAdvisorChecksResponse(TypedDict, closed=True):
    checks: "capo_support.types.trusted_advisor_check_list.TrustedAdvisorCheckList"
    """<p>Information about all available Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorChecksResponse) -> dict:
    out: dict = {}
    import capo_support.types.trusted_advisor_check_list

    out["checks"] = (
        capo_support.types.trusted_advisor_check_list.serialize_aws_json_1_1(
            value["checks"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorChecksResponse:
    out: DescribeTrustedAdvisorChecksResponse = {}  # type: ignore[typeddict-item]
    if data.get("checks") is not None:
        import capo_support.types.trusted_advisor_check_list

        out["checks"] = (
            capo_support.types.trusted_advisor_check_list.deserialize_aws_json_1_1(
                data["checks"]
            )
        )
    else:
        out["checks"] = []
    return out
