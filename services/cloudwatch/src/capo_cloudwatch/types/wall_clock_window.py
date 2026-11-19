"""Generated from Smithy shape ``com.amazonaws.cloudwatch#WallClockWindow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.timezone


class WallClockWindow(TypedDict, closed=True):
    timezone: NotRequired["capo_cloudwatch.types.timezone.Timezone"]
    """<p>The time zone to use when the alarm aligns the evaluation window to clock boundaries. You can specify an IANA time zone name (for example, <code>America/New_York</code>), a fixed UTC offset (for example, <code>+05:30</code>), or an offset-prefixed identifier (for example, <code>UTC+05:30</code>). The offset must be aligned to a multiple of 5 minutes. If you don't specify a time zone, CloudWatch uses <code>UTC</code>.</p> <p>The time zone affects window alignment for all periods, including periods of one hour or shorter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WallClockWindow) -> dict:
    out: dict = {}
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WallClockWindow:
    out: WallClockWindow = {}  # type: ignore[typeddict-item]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: WallClockWindow, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timezone" in value:
        pairs.append((f"{key_prefix}Timezone", str(value["timezone"])))


def deserialize_query(el: Element) -> WallClockWindow:
    out: WallClockWindow = {}  # type: ignore[typeddict-item]
    child_timezone = el.find("Timezone")
    if child_timezone is not None:
        out["timezone"] = str(child_timezone.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WallClockWindow) -> dict:
    out: dict = {}
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    return out


def deserialize_cbor(data: dict) -> WallClockWindow:
    out: WallClockWindow = {}  # type: ignore[typeddict-item]
    if data.get("Timezone") is not None:
        out["timezone"] = data["Timezone"]
    return out
