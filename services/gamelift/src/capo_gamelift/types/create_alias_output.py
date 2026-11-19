"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.alias


class CreateAliasOutput(TypedDict, closed=True):
    alias: NotRequired["capo_gamelift.types.alias.Alias"]
    """<p>The newly created alias resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasOutput) -> dict:
    out: dict = {}
    if "alias" in value:
        import capo_gamelift.types.alias

        out["Alias"] = capo_gamelift.types.alias.serialize_aws_json_1_1(value["alias"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasOutput:
    out: CreateAliasOutput = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        import capo_gamelift.types.alias

        out["alias"] = capo_gamelift.types.alias.deserialize_aws_json_1_1(data["Alias"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateAliasOutput) -> dict:
    out: dict = {}
    if "alias" in value:
        import capo_gamelift.types.alias

        out["Alias"] = capo_gamelift.types.alias.serialize_cbor(value["alias"])
    return out


def deserialize_cbor(data: dict) -> CreateAliasOutput:
    out: CreateAliasOutput = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        import capo_gamelift.types.alias

        out["alias"] = capo_gamelift.types.alias.deserialize_cbor(data["Alias"])
    return out
