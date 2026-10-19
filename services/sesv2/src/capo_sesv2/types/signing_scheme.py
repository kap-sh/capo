"""Generated from Smithy shape ``com.amazonaws.sesv2#SigningScheme``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError, SerializationError
from capo_sesv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sesv2.types.default_signing_scheme
    import capo_sesv2.types.smime_signing_scheme


class _SigningScheme_DefaultScheme(TypedDict, closed=True):
    DefaultScheme: "capo_sesv2.types.default_signing_scheme.DefaultSigningScheme"


class _SigningScheme_SmimeScheme(TypedDict, closed=True):
    SmimeScheme: "capo_sesv2.types.smime_signing_scheme.SmimeSigningScheme"


SigningScheme: TypeAlias = (
    _SigningScheme_DefaultScheme | _SigningScheme_SmimeScheme | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SigningScheme) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SigningScheme: cannot serialize unknown variant {value.name!r}"
        )
    elif "DefaultScheme" in value:
        import capo_sesv2.types.default_signing_scheme

        return {
            "DefaultScheme": capo_sesv2.types.default_signing_scheme.serialize_json(
                value["DefaultScheme"]
            )
        }
    elif "SmimeScheme" in value:
        import capo_sesv2.types.smime_signing_scheme

        return {
            "SmimeScheme": capo_sesv2.types.smime_signing_scheme.serialize_json(
                value["SmimeScheme"]
            )
        }
    else:
        raise SerializationError("SigningScheme: no variant present")


def deserialize_json(data: dict) -> SigningScheme:
    if data.get("DefaultScheme") is not None:
        import capo_sesv2.types.default_signing_scheme

        return {
            "DefaultScheme": capo_sesv2.types.default_signing_scheme.deserialize_json(
                data["DefaultScheme"]
            )
        }
    elif data.get("SmimeScheme") is not None:
        import capo_sesv2.types.smime_signing_scheme

        return {
            "SmimeScheme": capo_sesv2.types.smime_signing_scheme.deserialize_json(
                data["SmimeScheme"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SigningScheme: no recognized variant key")
