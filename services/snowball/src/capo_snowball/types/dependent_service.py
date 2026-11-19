"""Generated from Smithy shape ``com.amazonaws.snowball#DependentService``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.service_name
    import capo_snowball.types.service_version


class DependentService(TypedDict, closed=True):
    service_name: NotRequired["capo_snowball.types.service_name.ServiceName"]
    """<p>The name of the dependent service.</p>"""
    service_version: NotRequired["capo_snowball.types.service_version.ServiceVersion"]
    """<p>The version of the dependent service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependentService) -> dict:
    out: dict = {}
    if "service_name" in value:
        import capo_snowball.types.service_name

        out["ServiceName"] = capo_snowball.types.service_name.serialize_aws_json_1_1(
            value["service_name"]
        )
    if "service_version" in value:
        import capo_snowball.types.service_version

        out["ServiceVersion"] = (
            capo_snowball.types.service_version.serialize_aws_json_1_1(
                value["service_version"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DependentService:
    out: DependentService = {}  # type: ignore[typeddict-item]
    if data.get("ServiceName") is not None:
        import capo_snowball.types.service_name

        out["service_name"] = capo_snowball.types.service_name.deserialize_aws_json_1_1(
            data["ServiceName"]
        )
    if data.get("ServiceVersion") is not None:
        import capo_snowball.types.service_version

        out["service_version"] = (
            capo_snowball.types.service_version.deserialize_aws_json_1_1(
                data["ServiceVersion"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DependentService) -> dict:
    out: dict = {}
    if "service_name" in value:
        import capo_snowball.types.service_name

        out["ServiceName"] = capo_snowball.types.service_name.serialize_cbor(
            value["service_name"]
        )
    if "service_version" in value:
        import capo_snowball.types.service_version

        out["ServiceVersion"] = capo_snowball.types.service_version.serialize_cbor(
            value["service_version"]
        )
    return out


def deserialize_cbor(data: dict) -> DependentService:
    out: DependentService = {}  # type: ignore[typeddict-item]
    if data.get("ServiceName") is not None:
        import capo_snowball.types.service_name

        out["service_name"] = capo_snowball.types.service_name.deserialize_cbor(
            data["ServiceName"]
        )
    if data.get("ServiceVersion") is not None:
        import capo_snowball.types.service_version

        out["service_version"] = capo_snowball.types.service_version.deserialize_cbor(
            data["ServiceVersion"]
        )
    return out
