"""Generated from Smithy shape ``com.amazonaws.ssm#GetPatchBaselineForPatchGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.operating_system
    import capo_ssm.types.patch_group


class GetPatchBaselineForPatchGroupRequest(TypedDict, closed=True):
    patch_group: "capo_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group whose patch baseline should be retrieved.</p>"""
    operating_system: NotRequired["capo_ssm.types.operating_system.OperatingSystem"]
    """<p>Returns the operating system rule specified for patch groups using the patch baseline. The default value is <code>WINDOWS</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPatchBaselineForPatchGroupRequest) -> dict:
    out: dict = {}
    out["PatchGroup"] = value["patch_group"]
    if "operating_system" in value:
        import capo_ssm.types.operating_system

        out["OperatingSystem"] = capo_ssm.types.operating_system.serialize_aws_json_1_1(
            value["operating_system"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPatchBaselineForPatchGroupRequest:
    out: GetPatchBaselineForPatchGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("PatchGroup") is not None:
        out["patch_group"] = data["PatchGroup"]
    else:
        out["patch_group"] = ""
    if data.get("OperatingSystem") is not None:
        import capo_ssm.types.operating_system

        out["operating_system"] = (
            capo_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    return out
