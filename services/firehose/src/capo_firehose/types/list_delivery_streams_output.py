"""Generated from Smithy shape ``com.amazonaws.firehose#ListDeliveryStreamsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object
    import capo_firehose.types.delivery_stream_name_list


class ListDeliveryStreamsOutput(TypedDict, closed=True):
    delivery_stream_names: (
        "capo_firehose.types.delivery_stream_name_list.DeliveryStreamNameList"
    )
    """<p>The names of the Firehose streams.</p>"""
    has_more_delivery_streams: "capo_firehose.types.boolean_object.BooleanObject"
    """<p>Indicates whether there are more Firehose streams available to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeliveryStreamsOutput) -> dict:
    out: dict = {}
    import capo_firehose.types.delivery_stream_name_list

    out["DeliveryStreamNames"] = (
        capo_firehose.types.delivery_stream_name_list.serialize_aws_json_1_1(
            value["delivery_stream_names"]
        )
    )
    out["HasMoreDeliveryStreams"] = value["has_more_delivery_streams"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeliveryStreamsOutput:
    out: ListDeliveryStreamsOutput = {}  # type: ignore[typeddict-item]
    if data.get("DeliveryStreamNames") is not None:
        import capo_firehose.types.delivery_stream_name_list

        out["delivery_stream_names"] = (
            capo_firehose.types.delivery_stream_name_list.deserialize_aws_json_1_1(
                data["DeliveryStreamNames"]
            )
        )
    else:
        out["delivery_stream_names"] = []
    if data.get("HasMoreDeliveryStreams") is not None:
        out["has_more_delivery_streams"] = data["HasMoreDeliveryStreams"]
    else:
        out["has_more_delivery_streams"] = False
    return out
