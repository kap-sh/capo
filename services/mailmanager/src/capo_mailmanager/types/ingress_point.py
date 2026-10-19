"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_a_record
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_status
    import capo_mailmanager.types.ingress_point_type


class IngressPoint(TypedDict, closed=True):
    ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName"
    """<p>A user friendly name for the ingress endpoint resource.</p>"""
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier of the ingress endpoint resource.</p>"""
    status: "capo_mailmanager.types.ingress_point_status.IngressPointStatus"
    """<p>The status of the ingress endpoint resource.</p>"""
    type: "capo_mailmanager.types.ingress_point_type.IngressPointType"
    """<p>The type of ingress endpoint resource.</p>"""
    a_record: NotRequired[
        "capo_mailmanager.types.ingress_point_a_record.IngressPointARecord"
    ]
    """<p> The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPoint) -> dict:
    out: dict = {}
    out["IngressPointName"] = value["ingress_point_name"]
    out["IngressPointId"] = value["ingress_point_id"]
    import capo_mailmanager.types.ingress_point_status

    out["Status"] = capo_mailmanager.types.ingress_point_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_mailmanager.types.ingress_point_type

    out["Type"] = capo_mailmanager.types.ingress_point_type.serialize_aws_json_1_0(
        value["type"]
    )
    if "a_record" in value:
        out["ARecord"] = value["a_record"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngressPoint:
    out: IngressPoint = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointName") is not None:
        out["ingress_point_name"] = data["IngressPointName"]
    else:
        out["ingress_point_name"] = ""
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    if data.get("Status") is not None:
        import capo_mailmanager.types.ingress_point_status

        out["status"] = (
            capo_mailmanager.types.ingress_point_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_mailmanager.types.ingress_point_status.IngressPointStatus", ""
        )
    if data.get("Type") is not None:
        import capo_mailmanager.types.ingress_point_type

        out["type"] = (
            capo_mailmanager.types.ingress_point_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_mailmanager.types.ingress_point_type.IngressPointType", ""
        )
    if data.get("ARecord") is not None:
        out["a_record"] = data["ARecord"]
    return out
