"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateHostOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.host_arn
    import capo_codeconnections.types.tag_list


class CreateHostOutput(TypedDict, closed=True):
    host_arn: NotRequired["capo_codeconnections.types.host_arn.HostArn"]
    """<p>The Amazon Resource Name (ARN) of the host to be created.</p>"""
    tags: NotRequired["capo_codeconnections.types.tag_list.TagList"]
    """<p>Tags for the created host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateHostOutput) -> dict:
    out: dict = {}
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateHostOutput:
    out: CreateHostOutput = {}  # type: ignore[typeddict-item]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    if data.get("Tags") is not None:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateHostOutput) -> dict:
    out: dict = {}
    if "host_arn" in value:
        out["HostArn"] = value["host_arn"]
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> CreateHostOutput:
    out: CreateHostOutput = {}  # type: ignore[typeddict-item]
    if data.get("HostArn") is not None:
        out["host_arn"] = data["HostArn"]
    if data.get("Tags") is not None:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_cbor(data["Tags"])
    return out
