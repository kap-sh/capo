"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StartCompositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_client_token
    import capo_ivs_realtime.types.destination_configuration_list
    import capo_ivs_realtime.types.layout_configuration
    import capo_ivs_realtime.types.stage_arn
    import capo_ivs_realtime.types.tags


class StartCompositionRequest(TypedDict, closed=True):
    stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to be used for compositing.</p>"""
    idempotency_token: NotRequired[
        "capo_ivs_realtime.types.composition_client_token.CompositionClientToken"
    ]
    """<p>Idempotency token.</p>"""
    layout: NotRequired[
        "capo_ivs_realtime.types.layout_configuration.LayoutConfiguration"
    ]
    """<p>Layout object to configure composition parameters.</p>"""
    destinations: "capo_ivs_realtime.types.destination_configuration_list.DestinationConfigurationList"
    """<p>Array of destination configuration.</p>"""
    tags: NotRequired["capo_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCompositionRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    if "layout" in value:
        import capo_ivs_realtime.types.layout_configuration

        out["layout"] = capo_ivs_realtime.types.layout_configuration.serialize_json(
            value["layout"]
        )
    import capo_ivs_realtime.types.destination_configuration_list

    out["destinations"] = (
        capo_ivs_realtime.types.destination_configuration_list.serialize_json(
            value["destinations"]
        )
    )
    if "tags" in value:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartCompositionRequest:
    out: StartCompositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("StartCompositionRequest.stage_arn required")
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    if data.get("layout") is not None:
        import capo_ivs_realtime.types.layout_configuration

        out["layout"] = capo_ivs_realtime.types.layout_configuration.deserialize_json(
            data["layout"]
        )
    if data.get("destinations") is not None:
        import capo_ivs_realtime.types.destination_configuration_list

        out["destinations"] = (
            capo_ivs_realtime.types.destination_configuration_list.deserialize_json(
                data["destinations"]
            )
        )
    else:
        raise DeserializationError("StartCompositionRequest.destinations required")
    if data.get("tags") is not None:
        import capo_ivs_realtime.types.tags

        out["tags"] = capo_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
