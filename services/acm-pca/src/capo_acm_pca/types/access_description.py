"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm_pca.types.access_method
    import capo_acm_pca.types.general_name


class AccessDescription(TypedDict, closed=True):
    access_method: "capo_acm_pca.types.access_method.AccessMethod"
    """<p>The type and format of <code>AccessDescription</code> information.</p>"""
    access_location: "capo_acm_pca.types.general_name.GeneralName"
    """<p>The location of <code>AccessDescription</code> information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessDescription) -> dict:
    out: dict = {}
    import capo_acm_pca.types.access_method

    out["AccessMethod"] = capo_acm_pca.types.access_method.serialize_aws_json_1_1(
        value["access_method"]
    )
    import capo_acm_pca.types.general_name

    out["AccessLocation"] = capo_acm_pca.types.general_name.serialize_aws_json_1_1(
        value["access_location"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessDescription:
    out: AccessDescription = {}  # type: ignore[typeddict-item]
    if data.get("AccessMethod") is not None:
        import capo_acm_pca.types.access_method

        out["access_method"] = (
            capo_acm_pca.types.access_method.deserialize_aws_json_1_1(
                data["AccessMethod"]
            )
        )
    else:
        raise DeserializationError("AccessDescription.access_method required")
    if data.get("AccessLocation") is not None:
        import capo_acm_pca.types.general_name

        out["access_location"] = (
            capo_acm_pca.types.general_name.deserialize_aws_json_1_1(
                data["AccessLocation"]
            )
        )
    else:
        raise DeserializationError("AccessDescription.access_location required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessDescription) -> dict:
    out: dict = {}
    import capo_acm_pca.types.access_method

    out["AccessMethod"] = capo_acm_pca.types.access_method.serialize_cbor(
        value["access_method"]
    )
    import capo_acm_pca.types.general_name

    out["AccessLocation"] = capo_acm_pca.types.general_name.serialize_cbor(
        value["access_location"]
    )
    return out


def deserialize_cbor(data: dict) -> AccessDescription:
    out: AccessDescription = {}  # type: ignore[typeddict-item]
    if data.get("AccessMethod") is not None:
        import capo_acm_pca.types.access_method

        out["access_method"] = capo_acm_pca.types.access_method.deserialize_cbor(
            data["AccessMethod"]
        )
    else:
        raise DeserializationError("AccessDescription.access_method required")
    if data.get("AccessLocation") is not None:
        import capo_acm_pca.types.general_name

        out["access_location"] = capo_acm_pca.types.general_name.deserialize_cbor(
            data["AccessLocation"]
        )
    else:
        raise DeserializationError("AccessDescription.access_location required")
    return out
