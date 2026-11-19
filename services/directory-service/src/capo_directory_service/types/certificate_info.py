"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_cn
    import capo_directory_service.types.certificate_expiry_date_time
    import capo_directory_service.types.certificate_id
    import capo_directory_service.types.certificate_state
    import capo_directory_service.types.certificate_type


class CertificateInfo(TypedDict, closed=True):
    certificate_id: NotRequired[
        "capo_directory_service.types.certificate_id.CertificateId"
    ]
    """<p>The identifier of the certificate.</p>"""
    common_name: NotRequired[
        "capo_directory_service.types.certificate_cn.CertificateCN"
    ]
    """<p>The common name for the certificate.</p>"""
    state: NotRequired[
        "capo_directory_service.types.certificate_state.CertificateState"
    ]
    """<p>The state of the certificate.</p>"""
    expiry_date_time: NotRequired[
        "capo_directory_service.types.certificate_expiry_date_time.CertificateExpiryDateTime"
    ]
    """<p>The date and time when the certificate will expire.</p>"""
    type: NotRequired["capo_directory_service.types.certificate_type.CertificateType"]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateInfo) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "state" in value:
        import capo_directory_service.types.certificate_state

        out["State"] = (
            capo_directory_service.types.certificate_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "expiry_date_time" in value:
        import capo_directory_service.types.certificate_expiry_date_time

        out["ExpiryDateTime"] = (
            capo_directory_service.types.certificate_expiry_date_time.serialize_aws_json_1_1(
                value["expiry_date_time"]
            )
        )
    if "type" in value:
        import capo_directory_service.types.certificate_type

        out["Type"] = (
            capo_directory_service.types.certificate_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateInfo:
    out: CertificateInfo = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    if data.get("State") is not None:
        import capo_directory_service.types.certificate_state

        out["state"] = (
            capo_directory_service.types.certificate_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("ExpiryDateTime") is not None:
        import capo_directory_service.types.certificate_expiry_date_time

        out["expiry_date_time"] = (
            capo_directory_service.types.certificate_expiry_date_time.deserialize_aws_json_1_1(
                data["ExpiryDateTime"]
            )
        )
    if data.get("Type") is not None:
        import capo_directory_service.types.certificate_type

        out["type"] = (
            capo_directory_service.types.certificate_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateInfo) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "state" in value:
        import capo_directory_service.types.certificate_state

        out["State"] = capo_directory_service.types.certificate_state.serialize_cbor(
            value["state"]
        )
    if "expiry_date_time" in value:
        import capo_directory_service.types.certificate_expiry_date_time

        out["ExpiryDateTime"] = (
            capo_directory_service.types.certificate_expiry_date_time.serialize_cbor(
                value["expiry_date_time"]
            )
        )
    if "type" in value:
        import capo_directory_service.types.certificate_type

        out["Type"] = capo_directory_service.types.certificate_type.serialize_cbor(
            value["type"]
        )
    return out


def deserialize_cbor(data: dict) -> CertificateInfo:
    out: CertificateInfo = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    if data.get("State") is not None:
        import capo_directory_service.types.certificate_state

        out["state"] = capo_directory_service.types.certificate_state.deserialize_cbor(
            data["State"]
        )
    if data.get("ExpiryDateTime") is not None:
        import capo_directory_service.types.certificate_expiry_date_time

        out["expiry_date_time"] = (
            capo_directory_service.types.certificate_expiry_date_time.deserialize_cbor(
                data["ExpiryDateTime"]
            )
        )
    if data.get("Type") is not None:
        import capo_directory_service.types.certificate_type

        out["type"] = capo_directory_service.types.certificate_type.deserialize_cbor(
            data["Type"]
        )
    return out
