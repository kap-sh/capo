"""Generated from Smithy shape ``com.amazonaws.kendra#ListAccessControlConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.access_control_configuration_summary_list
    import capo_kendra.types.string


class ListAccessControlConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_kendra.types.string.String"]
    """<p>If the response is truncated, Amazon Kendra returns this token, which you can use in the subsequent request to retrieve the next set of access control configurations.</p>"""
    access_control_configurations: "capo_kendra.types.access_control_configuration_summary_list.AccessControlConfigurationSummaryList"
    """<p>The details of your access control configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessControlConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_kendra.types.access_control_configuration_summary_list

    out["AccessControlConfigurations"] = (
        capo_kendra.types.access_control_configuration_summary_list.serialize_aws_json_1_1(
            value["access_control_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessControlConfigurationsResponse:
    out: ListAccessControlConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AccessControlConfigurations") is not None:
        import capo_kendra.types.access_control_configuration_summary_list

        out["access_control_configurations"] = (
            capo_kendra.types.access_control_configuration_summary_list.deserialize_aws_json_1_1(
                data["AccessControlConfigurations"]
            )
        )
    else:
        out["access_control_configurations"] = []
    return out
