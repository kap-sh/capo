"""Generated from Smithy shape ``com.amazonaws.ssm#StartAccessRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.string1to256
    import capo_ssm.types.tag_list
    import capo_ssm.types.targets


class StartAccessRequestRequest(TypedDict, closed=True):
    reason: "capo_ssm.types.string1to256.String1to256"
    """<p>A brief description explaining why you are requesting access to the node.</p>"""
    targets: "capo_ssm.types.targets.Targets"
    """<p>The node you are requesting access to.</p>"""
    tags: NotRequired["capo_ssm.types.tag_list.TagList"]
    """<p>Key-value pairs of metadata you want to assign to the access request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAccessRequestRequest) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    import capo_ssm.types.targets

    out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "tags" in value:
        import capo_ssm.types.tag_list

        out["Tags"] = capo_ssm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAccessRequestRequest:
    out: StartAccessRequestRequest = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        out["reason"] = ""
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        out["targets"] = []
    if data.get("Tags") is not None:
        import capo_ssm.types.tag_list

        out["tags"] = capo_ssm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
