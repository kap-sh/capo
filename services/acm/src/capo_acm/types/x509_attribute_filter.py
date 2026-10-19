"""Generated from Smithy shape ``com.amazonaws.acm#X509AttributeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.extended_key_usage_name
    import capo_acm.types.key_algorithm
    import capo_acm.types.key_usage_name
    import capo_acm.types.serial_number
    import capo_acm.types.subject_alternative_name_filter
    import capo_acm.types.subject_filter
    import capo_acm.types.timestamp_range


class _X509AttributeFilter_Subject(TypedDict, closed=True):
    Subject: "capo_acm.types.subject_filter.SubjectFilter"


class _X509AttributeFilter_SubjectAlternativeName(TypedDict, closed=True):
    SubjectAlternativeName: (
        "capo_acm.types.subject_alternative_name_filter.SubjectAlternativeNameFilter"
    )


class _X509AttributeFilter_ExtendedKeyUsage(TypedDict, closed=True):
    ExtendedKeyUsage: "capo_acm.types.extended_key_usage_name.ExtendedKeyUsageName"


class _X509AttributeFilter_KeyUsage(TypedDict, closed=True):
    KeyUsage: "capo_acm.types.key_usage_name.KeyUsageName"


class _X509AttributeFilter_KeyAlgorithm(TypedDict, closed=True):
    KeyAlgorithm: "capo_acm.types.key_algorithm.KeyAlgorithm"


class _X509AttributeFilter_SerialNumber(TypedDict, closed=True):
    SerialNumber: "capo_acm.types.serial_number.SerialNumber"


class _X509AttributeFilter_NotAfter(TypedDict, closed=True):
    NotAfter: "capo_acm.types.timestamp_range.TimestampRange"


class _X509AttributeFilter_NotBefore(TypedDict, closed=True):
    NotBefore: "capo_acm.types.timestamp_range.TimestampRange"


X509AttributeFilter: TypeAlias = (
    _X509AttributeFilter_Subject
    | _X509AttributeFilter_SubjectAlternativeName
    | _X509AttributeFilter_ExtendedKeyUsage
    | _X509AttributeFilter_KeyUsage
    | _X509AttributeFilter_KeyAlgorithm
    | _X509AttributeFilter_SerialNumber
    | _X509AttributeFilter_NotAfter
    | _X509AttributeFilter_NotBefore
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: X509AttributeFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"X509AttributeFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "Subject" in value:
        import capo_acm.types.subject_filter

        return {
            "Subject": capo_acm.types.subject_filter.serialize_aws_json_1_1(
                value["Subject"]
            )
        }
    elif "SubjectAlternativeName" in value:
        import capo_acm.types.subject_alternative_name_filter

        return {
            "SubjectAlternativeName": capo_acm.types.subject_alternative_name_filter.serialize_aws_json_1_1(
                value["SubjectAlternativeName"]
            )
        }
    elif "ExtendedKeyUsage" in value:
        import capo_acm.types.extended_key_usage_name

        return {
            "ExtendedKeyUsage": capo_acm.types.extended_key_usage_name.serialize_aws_json_1_1(
                value["ExtendedKeyUsage"]
            )
        }
    elif "KeyUsage" in value:
        import capo_acm.types.key_usage_name

        return {
            "KeyUsage": capo_acm.types.key_usage_name.serialize_aws_json_1_1(
                value["KeyUsage"]
            )
        }
    elif "KeyAlgorithm" in value:
        import capo_acm.types.key_algorithm

        return {
            "KeyAlgorithm": capo_acm.types.key_algorithm.serialize_aws_json_1_1(
                value["KeyAlgorithm"]
            )
        }
    elif "SerialNumber" in value:
        return {"SerialNumber": value["SerialNumber"]}
    elif "NotAfter" in value:
        import capo_acm.types.timestamp_range

        return {
            "NotAfter": capo_acm.types.timestamp_range.serialize_aws_json_1_1(
                value["NotAfter"]
            )
        }
    elif "NotBefore" in value:
        import capo_acm.types.timestamp_range

        return {
            "NotBefore": capo_acm.types.timestamp_range.serialize_aws_json_1_1(
                value["NotBefore"]
            )
        }
    else:
        raise SerializationError("X509AttributeFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> X509AttributeFilter:
    if data.get("Subject") is not None:
        import capo_acm.types.subject_filter

        return {
            "Subject": capo_acm.types.subject_filter.deserialize_aws_json_1_1(
                data["Subject"]
            )
        }
    elif data.get("SubjectAlternativeName") is not None:
        import capo_acm.types.subject_alternative_name_filter

        return {
            "SubjectAlternativeName": capo_acm.types.subject_alternative_name_filter.deserialize_aws_json_1_1(
                data["SubjectAlternativeName"]
            )
        }
    elif data.get("ExtendedKeyUsage") is not None:
        import capo_acm.types.extended_key_usage_name

        return {
            "ExtendedKeyUsage": capo_acm.types.extended_key_usage_name.deserialize_aws_json_1_1(
                data["ExtendedKeyUsage"]
            )
        }
    elif data.get("KeyUsage") is not None:
        import capo_acm.types.key_usage_name

        return {
            "KeyUsage": capo_acm.types.key_usage_name.deserialize_aws_json_1_1(
                data["KeyUsage"]
            )
        }
    elif data.get("KeyAlgorithm") is not None:
        import capo_acm.types.key_algorithm

        return {
            "KeyAlgorithm": capo_acm.types.key_algorithm.deserialize_aws_json_1_1(
                data["KeyAlgorithm"]
            )
        }
    elif data.get("SerialNumber") is not None:
        return {"SerialNumber": data["SerialNumber"]}
    elif data.get("NotAfter") is not None:
        import capo_acm.types.timestamp_range

        return {
            "NotAfter": capo_acm.types.timestamp_range.deserialize_aws_json_1_1(
                data["NotAfter"]
            )
        }
    elif data.get("NotBefore") is not None:
        import capo_acm.types.timestamp_range

        return {
            "NotBefore": capo_acm.types.timestamp_range.deserialize_aws_json_1_1(
                data["NotBefore"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("X509AttributeFilter: no recognized variant key")
