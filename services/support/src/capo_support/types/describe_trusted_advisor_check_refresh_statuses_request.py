"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckRefreshStatusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.string_list


class DescribeTrustedAdvisorCheckRefreshStatusesRequest(TypedDict, closed=True):
    check_ids: "capo_support.types.string_list.StringList"
    """<p>The IDs of the Trusted Advisor checks to get the status.</p> <note> <p>If you specify the check ID of a check that is automatically refreshed, you might see an <code>InvalidParameterValue</code> error.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTrustedAdvisorCheckRefreshStatusesRequest,
) -> dict:
    out: dict = {}
    import capo_support.types.string_list

    out["checkIds"] = capo_support.types.string_list.serialize_aws_json_1_1(
        value["check_ids"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckRefreshStatusesRequest:
    out: DescribeTrustedAdvisorCheckRefreshStatusesRequest = {}  # type: ignore[typeddict-item]
    if data.get("checkIds") is not None:
        import capo_support.types.string_list

        out["check_ids"] = capo_support.types.string_list.deserialize_aws_json_1_1(
            data["checkIds"]
        )
    else:
        out["check_ids"] = []
    return out
