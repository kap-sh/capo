"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.string_list


class DescribeTrustedAdvisorCheckSummariesRequest(TypedDict, closed=True):
    check_ids: "capo_support.types.string_list.StringList"
    """<p>The IDs of the Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorCheckSummariesRequest) -> dict:
    out: dict = {}
    import capo_support.types.string_list

    out["checkIds"] = capo_support.types.string_list.serialize_aws_json_1_1(
        value["check_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorCheckSummariesRequest:
    out: DescribeTrustedAdvisorCheckSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkIds") is not None:
        import capo_support.types.string_list

        out["check_ids"] = capo_support.types.string_list.deserialize_aws_json_1_1(
            data["checkIds"]
        )
    else:
        out["check_ids"] = []
    return out
