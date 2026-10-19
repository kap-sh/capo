"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountDedicatedIpWarmupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled


class PutAccountDedicatedIpWarmupAttributesRequest(TypedDict, closed=True):
    auto_warmup_enabled: NotRequired["capo_sesv2.types.enabled.Enabled"]
    """<p>Enables or disables the automatic warm-up feature for dedicated IP addresses that are associated with your Amazon SES account in the current Amazon Web Services Region. Set to <code>true</code> to enable the automatic warm-up feature, or set to <code>false</code> to disable it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDedicatedIpWarmupAttributesRequest) -> dict:
    out: dict = {}
    if "auto_warmup_enabled" in value:
        out["AutoWarmupEnabled"] = value["auto_warmup_enabled"]
    return out


def deserialize_json(data: dict) -> PutAccountDedicatedIpWarmupAttributesRequest:
    out: PutAccountDedicatedIpWarmupAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoWarmupEnabled") is not None:
        out["auto_warmup_enabled"] = data["AutoWarmupEnabled"]
    return out
