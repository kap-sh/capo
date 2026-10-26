"""Generated from Smithy shape ``com.amazonaws.omics#FormatOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError
from capo_omics.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_omics.types.tsv_options
    import capo_omics.types.vcf_options


class _FormatOptions_tsvOptions(TypedDict, closed=True):
    tsvOptions: "capo_omics.types.tsv_options.TsvOptions"


class _FormatOptions_vcfOptions(TypedDict, closed=True):
    vcfOptions: "capo_omics.types.vcf_options.VcfOptions"


FormatOptions: TypeAlias = (
    _FormatOptions_tsvOptions | _FormatOptions_vcfOptions | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FormatOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FormatOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tsvOptions" in value:
        import capo_omics.types.tsv_options

        return {
            "tsvOptions": capo_omics.types.tsv_options.serialize_json(
                value["tsvOptions"]
            )
        }
    elif "vcfOptions" in value:
        import capo_omics.types.vcf_options

        return {
            "vcfOptions": capo_omics.types.vcf_options.serialize_json(
                value["vcfOptions"]
            )
        }
    else:
        raise SerializationError("FormatOptions: no variant present")


def deserialize_json(data: dict) -> FormatOptions:
    if data.get("tsvOptions") is not None:
        import capo_omics.types.tsv_options

        return {
            "tsvOptions": capo_omics.types.tsv_options.deserialize_json(
                data["tsvOptions"]
            )
        }
    elif data.get("vcfOptions") is not None:
        import capo_omics.types.vcf_options

        return {
            "vcfOptions": capo_omics.types.vcf_options.deserialize_json(
                data["vcfOptions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FormatOptions: no recognized variant key")
