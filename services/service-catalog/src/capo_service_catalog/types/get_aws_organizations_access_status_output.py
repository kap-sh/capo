"""Generated from Smithy shape ``com.amazonaws.servicecatalog#GetAWSOrganizationsAccessStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.access_status


class GetAWSOrganizationsAccessStatusOutput(TypedDict, closed=True):
    access_status: NotRequired["capo_service_catalog.types.access_status.AccessStatus"]
    """<p>The status of the portfolio share feature.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAWSOrganizationsAccessStatusOutput) -> dict:
    out: dict = {}
    if "access_status" in value:
        import capo_service_catalog.types.access_status

        out["AccessStatus"] = (
            capo_service_catalog.types.access_status.serialize_aws_json_1_1(
                value["access_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAWSOrganizationsAccessStatusOutput:
    out: GetAWSOrganizationsAccessStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("AccessStatus") is not None:
        import capo_service_catalog.types.access_status

        out["access_status"] = (
            capo_service_catalog.types.access_status.deserialize_aws_json_1_1(
                data["AccessStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAWSOrganizationsAccessStatusOutput) -> dict:
    out: dict = {}
    if "access_status" in value:
        import capo_service_catalog.types.access_status

        out["AccessStatus"] = capo_service_catalog.types.access_status.serialize_cbor(
            value["access_status"]
        )
    return out


def deserialize_cbor(data: dict) -> GetAWSOrganizationsAccessStatusOutput:
    out: GetAWSOrganizationsAccessStatusOutput = {}  # type: ignore[typeddict-item]
    if data.get("AccessStatus") is not None:
        import capo_service_catalog.types.access_status

        out["access_status"] = (
            capo_service_catalog.types.access_status.deserialize_cbor(
                data["AccessStatus"]
            )
        )
    return out
