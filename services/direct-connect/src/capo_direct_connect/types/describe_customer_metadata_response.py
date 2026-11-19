"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeCustomerMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.agreement_list
    import capo_direct_connect.types.nni_partner_type


class DescribeCustomerMetadataResponse(TypedDict, closed=True):
    agreements: NotRequired["capo_direct_connect.types.agreement_list.AgreementList"]
    """<p>The list of customer agreements.</p>"""
    nni_partner_type: NotRequired[
        "capo_direct_connect.types.nni_partner_type.NniPartnerType"
    ]
    """<p>The type of network-to-network interface (NNI) partner. The partner type will be one of the following:</p> <ul> <li> <p>V1: This partner can only allocate 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, or 500Mbps subgigabit connections.</p> </li> <li> <p>V2: This partner can only allocate 1GB, 2GB, 5GB, or 10GB hosted connections.</p> </li> <li> <p>nonPartner: The customer is not a partner.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomerMetadataResponse) -> dict:
    out: dict = {}
    if "agreements" in value:
        import capo_direct_connect.types.agreement_list

        out["agreements"] = (
            capo_direct_connect.types.agreement_list.serialize_aws_json_1_1(
                value["agreements"]
            )
        )
    if "nni_partner_type" in value:
        import capo_direct_connect.types.nni_partner_type

        out["nniPartnerType"] = (
            capo_direct_connect.types.nni_partner_type.serialize_aws_json_1_1(
                value["nni_partner_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomerMetadataResponse:
    out: DescribeCustomerMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("agreements") is not None:
        import capo_direct_connect.types.agreement_list

        out["agreements"] = (
            capo_direct_connect.types.agreement_list.deserialize_aws_json_1_1(
                data["agreements"]
            )
        )
    if data.get("nniPartnerType") is not None:
        import capo_direct_connect.types.nni_partner_type

        out["nni_partner_type"] = (
            capo_direct_connect.types.nni_partner_type.deserialize_aws_json_1_1(
                data["nniPartnerType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeCustomerMetadataResponse) -> dict:
    out: dict = {}
    if "agreements" in value:
        import capo_direct_connect.types.agreement_list

        out["agreements"] = capo_direct_connect.types.agreement_list.serialize_cbor(
            value["agreements"]
        )
    if "nni_partner_type" in value:
        import capo_direct_connect.types.nni_partner_type

        out["nniPartnerType"] = (
            capo_direct_connect.types.nni_partner_type.serialize_cbor(
                value["nni_partner_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeCustomerMetadataResponse:
    out: DescribeCustomerMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("agreements") is not None:
        import capo_direct_connect.types.agreement_list

        out["agreements"] = capo_direct_connect.types.agreement_list.deserialize_cbor(
            data["agreements"]
        )
    if data.get("nniPartnerType") is not None:
        import capo_direct_connect.types.nni_partner_type

        out["nni_partner_type"] = (
            capo_direct_connect.types.nni_partner_type.deserialize_cbor(
                data["nniPartnerType"]
            )
        )
    return out
