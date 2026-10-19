"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateResiliencyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.idempotency_token
    import capo_direct_connect.types.resiliency_group_name
    import capo_direct_connect.types.resiliency_model
    import capo_direct_connect.types.tag_list


class CreateResiliencyGroupRequest(TypedDict, closed=True):
    resiliency_group_name: (
        "capo_direct_connect.types.resiliency_group_name.ResiliencyGroupName"
    )
    """<p>The name of the resiliency group.</p>"""
    intended_resiliency_model: (
        "capo_direct_connect.types.resiliency_model.ResiliencyModel"
    )
    """<p>The resiliency model that the resiliency group is intended to meet. The valid values are <code>maximum-resiliency</code>, <code>high-resiliency</code>, and <code>basic-resiliency</code>.</p>"""
    client_token: NotRequired[
        "capo_direct_connect.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_direct_connect.types.tag_list.TagList"]
    """<p>The tags to associate with the resiliency group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResiliencyGroupRequest) -> dict:
    out: dict = {}
    out["resiliencyGroupName"] = value["resiliency_group_name"]
    import capo_direct_connect.types.resiliency_model

    out["intendedResiliencyModel"] = (
        capo_direct_connect.types.resiliency_model.serialize_aws_json_1_1(
            value["intended_resiliency_model"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResiliencyGroupRequest:
    out: CreateResiliencyGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupName") is not None:
        out["resiliency_group_name"] = data["resiliencyGroupName"]
    else:
        out["resiliency_group_name"] = ""
    if data.get("intendedResiliencyModel") is not None:
        import capo_direct_connect.types.resiliency_model

        out["intended_resiliency_model"] = (
            capo_direct_connect.types.resiliency_model.deserialize_aws_json_1_1(
                data["intendedResiliencyModel"]
            )
        )
    else:
        import typing

        out["intended_resiliency_model"] = typing.cast(
            "capo_direct_connect.types.resiliency_model.ResiliencyModel", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_direct_connect.types.tag_list

        out["tags"] = capo_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
