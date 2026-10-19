"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.operating_system
    import capo_ssm.types.patch_property
    import capo_ssm.types.patch_set


class DescribePatchPropertiesRequest(TypedDict, closed=True):
    operating_system: "capo_ssm.types.operating_system.OperatingSystem"
    """<p>The operating system type for which to list patches.</p>"""
    property: "capo_ssm.types.patch_property.PatchProperty"
    """<p>The patch property for which you want to view patch details. </p>"""
    patch_set: NotRequired["capo_ssm.types.patch_set.PatchSet"]
    """<p>Indicates whether to list patches for the Windows operating system or for applications released by Microsoft. Not applicable for the Linux or macOS operating systems.</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchPropertiesRequest) -> dict:
    out: dict = {}
    import capo_ssm.types.operating_system

    out["OperatingSystem"] = capo_ssm.types.operating_system.serialize_aws_json_1_1(
        value["operating_system"]
    )
    import capo_ssm.types.patch_property

    out["Property"] = capo_ssm.types.patch_property.serialize_aws_json_1_1(
        value["property"]
    )
    if "patch_set" in value:
        import capo_ssm.types.patch_set

        out["PatchSet"] = capo_ssm.types.patch_set.serialize_aws_json_1_1(
            value["patch_set"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchPropertiesRequest:
    out: DescribePatchPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("OperatingSystem") is not None:
        import capo_ssm.types.operating_system

        out["operating_system"] = (
            capo_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    else:
        import typing

        out["operating_system"] = typing.cast(
            "capo_ssm.types.operating_system.OperatingSystem", ""
        )
    if data.get("Property") is not None:
        import capo_ssm.types.patch_property

        out["property"] = capo_ssm.types.patch_property.deserialize_aws_json_1_1(
            data["Property"]
        )
    else:
        import typing

        out["property"] = typing.cast("capo_ssm.types.patch_property.PatchProperty", "")
    if data.get("PatchSet") is not None:
        import capo_ssm.types.patch_set

        out["patch_set"] = capo_ssm.types.patch_set.deserialize_aws_json_1_1(
            data["PatchSet"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
