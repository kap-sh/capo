"""Generated from Smithy shape ``com.amazonaws.servicediscovery#UpdateServiceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.service_attributes_map


class UpdateServiceAttributesRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that you want to update. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN.</p>"""
    attributes: (
        "capo_servicediscovery.types.service_attributes_map.ServiceAttributesMap"
    )
    """<p>A string map that contains attribute key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServiceAttributesRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    import capo_servicediscovery.types.service_attributes_map

    out["Attributes"] = (
        capo_servicediscovery.types.service_attributes_map.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServiceAttributesRequest:
    out: UpdateServiceAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        out["service_id"] = ""
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.service_attributes_map

        out["attributes"] = (
            capo_servicediscovery.types.service_attributes_map.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        out["attributes"] = {}
    return out
