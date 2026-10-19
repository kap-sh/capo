"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#PartnerLedSupport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.coverage
    import capo_partnercentral_channel.types.provider


class PartnerLedSupport(TypedDict, closed=True):
    coverage: "capo_partnercentral_channel.types.coverage.Coverage"
    """<p>The coverage level for partner-led support.</p>"""
    provider: NotRequired["capo_partnercentral_channel.types.provider.Provider"]
    """<p>The provider of the partner-led support.</p>"""
    tam_location: "str"
    """<p>The location of the Technical Account Manager (TAM).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerLedSupport) -> dict:
    out: dict = {}
    import capo_partnercentral_channel.types.coverage

    out["coverage"] = capo_partnercentral_channel.types.coverage.serialize_aws_json_1_0(
        value["coverage"]
    )
    if "provider" in value:
        import capo_partnercentral_channel.types.provider

        out["provider"] = (
            capo_partnercentral_channel.types.provider.serialize_aws_json_1_0(
                value["provider"]
            )
        )
    out["tamLocation"] = value["tam_location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerLedSupport:
    out: PartnerLedSupport = {}  # type: ignore[typeddict-item]
    if data.get("coverage") is not None:
        import capo_partnercentral_channel.types.coverage

        out["coverage"] = (
            capo_partnercentral_channel.types.coverage.deserialize_aws_json_1_0(
                data["coverage"]
            )
        )
    else:
        import typing

        out["coverage"] = typing.cast(
            "capo_partnercentral_channel.types.coverage.Coverage", ""
        )
    if data.get("provider") is not None:
        import capo_partnercentral_channel.types.provider

        out["provider"] = (
            capo_partnercentral_channel.types.provider.deserialize_aws_json_1_0(
                data["provider"]
            )
        )
    if data.get("tamLocation") is not None:
        out["tam_location"] = data["tamLocation"]
    else:
        out["tam_location"] = ""
    return out
