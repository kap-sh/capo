"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeInstancePatchesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_compliance_data_list


class DescribeInstancePatchesResult(TypedDict, closed=True):
    patches: NotRequired[
        "capo_ssm.types.patch_compliance_data_list.PatchComplianceDataList"
    ]
    """<p>Each entry in the array is a structure containing:</p> <ul> <li> <p>Title (string)</p> </li> <li> <p>KBId (string)</p> </li> <li> <p>Classification (string)</p> </li> <li> <p>Severity (string)</p> </li> <li> <p>State (string, such as "INSTALLED" or "FAILED")</p> </li> <li> <p>InstalledTime (DateTime)</p> </li> <li> <p>InstalledBy (string)</p> </li> </ul>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstancePatchesResult) -> dict:
    out: dict = {}
    if "patches" in value:
        import capo_ssm.types.patch_compliance_data_list

        out["Patches"] = (
            capo_ssm.types.patch_compliance_data_list.serialize_aws_json_1_1(
                value["patches"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstancePatchesResult:
    out: DescribeInstancePatchesResult = {}  # type: ignore[typeddict-item]
    if data.get("Patches") is not None:
        import capo_ssm.types.patch_compliance_data_list

        out["patches"] = (
            capo_ssm.types.patch_compliance_data_list.deserialize_aws_json_1_1(
                data["Patches"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
