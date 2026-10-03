"""Generated from Smithy shape ``com.amazonaws.connect#UpdateRoutingProfileConcurrencyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.media_concurrencies
    import capo_connect.types.routing_profile_id


class UpdateRoutingProfileConcurrencyRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    routing_profile_id: "capo_connect.types.routing_profile_id.RoutingProfileId"
    """<p>The identifier of the routing profile.</p>"""
    media_concurrencies: "capo_connect.types.media_concurrencies.MediaConcurrencies"
    """<p>The channels that agents can handle in the Contact Control Panel (CCP).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoutingProfileConcurrencyRequest) -> dict:
    out: dict = {}
    import capo_connect.types.media_concurrencies

    out["MediaConcurrencies"] = capo_connect.types.media_concurrencies.serialize_json(
        value["media_concurrencies"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRoutingProfileConcurrencyRequest:
    out: UpdateRoutingProfileConcurrencyRequest = {}  # type: ignore[typeddict-item]
    if data.get("MediaConcurrencies") is not None:
        import capo_connect.types.media_concurrencies

        out["media_concurrencies"] = (
            capo_connect.types.media_concurrencies.deserialize_json(
                data["MediaConcurrencies"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRoutingProfileConcurrencyRequest.media_concurrencies required"
        )
    return out
