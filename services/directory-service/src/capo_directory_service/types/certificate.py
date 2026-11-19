"""Generated from Smithy shape ``com.amazonaws.directoryservice#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.certificate_cn
    import capo_directory_service.types.certificate_expiry_date_time
    import capo_directory_service.types.certificate_id
    import capo_directory_service.types.certificate_registered_date_time
    import capo_directory_service.types.certificate_state
    import capo_directory_service.types.certificate_state_reason
    import capo_directory_service.types.certificate_type
    import capo_directory_service.types.client_cert_auth_settings


class Certificate(TypedDict, closed=True):
    certificate_id: NotRequired[
        "capo_directory_service.types.certificate_id.CertificateId"
    ]
    """<p>The identifier of the certificate.</p>"""
    state: NotRequired[
        "capo_directory_service.types.certificate_state.CertificateState"
    ]
    """<p>The state of the certificate.</p>"""
    state_reason: NotRequired[
        "capo_directory_service.types.certificate_state_reason.CertificateStateReason"
    ]
    """<p>Describes a state change for the certificate.</p>"""
    common_name: NotRequired[
        "capo_directory_service.types.certificate_cn.CertificateCN"
    ]
    """<p>The common name for the certificate.</p>"""
    registered_date_time: NotRequired[
        "capo_directory_service.types.certificate_registered_date_time.CertificateRegisteredDateTime"
    ]
    """<p>The date and time that the certificate was registered.</p>"""
    expiry_date_time: NotRequired[
        "capo_directory_service.types.certificate_expiry_date_time.CertificateExpiryDateTime"
    ]
    """<p>The date and time when the certificate will expire.</p>"""
    type: NotRequired["capo_directory_service.types.certificate_type.CertificateType"]
    """<p>The function that the registered certificate performs. Valid values include <code>ClientLDAPS</code> or <code>ClientCertAuth</code>. The default value is <code>ClientLDAPS</code>.</p>"""
    client_cert_auth_settings: NotRequired[
        "capo_directory_service.types.client_cert_auth_settings.ClientCertAuthSettings"
    ]
    """<p>A <code>ClientCertAuthSettings</code> object that contains client certificate authentication settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificate) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "state" in value:
        import capo_directory_service.types.certificate_state

        out["State"] = (
            capo_directory_service.types.certificate_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "registered_date_time" in value:
        import capo_directory_service.types.certificate_registered_date_time

        out["RegisteredDateTime"] = (
            capo_directory_service.types.certificate_registered_date_time.serialize_aws_json_1_1(
                value["registered_date_time"]
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
    if "client_cert_auth_settings" in value:
        import capo_directory_service.types.client_cert_auth_settings

        out["ClientCertAuthSettings"] = (
            capo_directory_service.types.client_cert_auth_settings.serialize_aws_json_1_1(
                value["client_cert_auth_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    if data.get("State") is not None:
        import capo_directory_service.types.certificate_state

        out["state"] = (
            capo_directory_service.types.certificate_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    if data.get("RegisteredDateTime") is not None:
        import capo_directory_service.types.certificate_registered_date_time

        out["registered_date_time"] = (
            capo_directory_service.types.certificate_registered_date_time.deserialize_aws_json_1_1(
                data["RegisteredDateTime"]
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
    if data.get("ClientCertAuthSettings") is not None:
        import capo_directory_service.types.client_cert_auth_settings

        out["client_cert_auth_settings"] = (
            capo_directory_service.types.client_cert_auth_settings.deserialize_aws_json_1_1(
                data["ClientCertAuthSettings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Certificate) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "state" in value:
        import capo_directory_service.types.certificate_state

        out["State"] = capo_directory_service.types.certificate_state.serialize_cbor(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "common_name" in value:
        out["CommonName"] = value["common_name"]
    if "registered_date_time" in value:
        import capo_directory_service.types.certificate_registered_date_time

        out["RegisteredDateTime"] = (
            capo_directory_service.types.certificate_registered_date_time.serialize_cbor(
                value["registered_date_time"]
            )
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
    if "client_cert_auth_settings" in value:
        import capo_directory_service.types.client_cert_auth_settings

        out["ClientCertAuthSettings"] = (
            capo_directory_service.types.client_cert_auth_settings.serialize_cbor(
                value["client_cert_auth_settings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if data.get("CertificateId") is not None:
        out["certificate_id"] = data["CertificateId"]
    if data.get("State") is not None:
        import capo_directory_service.types.certificate_state

        out["state"] = capo_directory_service.types.certificate_state.deserialize_cbor(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("CommonName") is not None:
        out["common_name"] = data["CommonName"]
    if data.get("RegisteredDateTime") is not None:
        import capo_directory_service.types.certificate_registered_date_time

        out["registered_date_time"] = (
            capo_directory_service.types.certificate_registered_date_time.deserialize_cbor(
                data["RegisteredDateTime"]
            )
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
    if data.get("ClientCertAuthSettings") is not None:
        import capo_directory_service.types.client_cert_auth_settings

        out["client_cert_auth_settings"] = (
            capo_directory_service.types.client_cert_auth_settings.deserialize_cbor(
                data["ClientCertAuthSettings"]
            )
        )
    return out
