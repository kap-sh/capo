"""Generated from Smithy shape ``com.amazonaws.acm#ValidationChallenge``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.dns_validation_challenge
    import capo_acm.types.email_validation_challenge


class _ValidationChallenge_EmailValidationChallenge(TypedDict, closed=True):
    EmailValidationChallenge: (
        "capo_acm.types.email_validation_challenge.EmailValidationChallenge"
    )


class _ValidationChallenge_DnsValidationChallenge(TypedDict, closed=True):
    DnsValidationChallenge: (
        "capo_acm.types.dns_validation_challenge.DnsValidationChallenge"
    )


ValidationChallenge: TypeAlias = (
    _ValidationChallenge_EmailValidationChallenge
    | _ValidationChallenge_DnsValidationChallenge
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationChallenge) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ValidationChallenge: cannot serialize unknown variant {value.name!r}"
        )
    elif "EmailValidationChallenge" in value:
        import capo_acm.types.email_validation_challenge

        return {
            "EmailValidationChallenge": capo_acm.types.email_validation_challenge.serialize_aws_json_1_1(
                value["EmailValidationChallenge"]
            )
        }
    elif "DnsValidationChallenge" in value:
        import capo_acm.types.dns_validation_challenge

        return {
            "DnsValidationChallenge": capo_acm.types.dns_validation_challenge.serialize_aws_json_1_1(
                value["DnsValidationChallenge"]
            )
        }
    else:
        raise SerializationError("ValidationChallenge: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ValidationChallenge:
    if data.get("EmailValidationChallenge") is not None:
        import capo_acm.types.email_validation_challenge

        return {
            "EmailValidationChallenge": capo_acm.types.email_validation_challenge.deserialize_aws_json_1_1(
                data["EmailValidationChallenge"]
            )
        }
    elif data.get("DnsValidationChallenge") is not None:
        import capo_acm.types.dns_validation_challenge

        return {
            "DnsValidationChallenge": capo_acm.types.dns_validation_challenge.deserialize_aws_json_1_1(
                data["DnsValidationChallenge"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ValidationChallenge: no recognized variant key")
