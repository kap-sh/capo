"""Generated from Smithy shape ``com.amazonaws.lightsail#WafBotControlConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.waf_inspection_level_enum


class WafBotControlConfig(TypedDict, closed=True):
    inspection_level: NotRequired[
        "capo_lightsail.types.waf_inspection_level_enum.WafInspectionLevelEnum"
    ]
    """<p>The inspection level of the bot control rule group.</p> <p>The following inspection levels are possible:</p> <ul> <li> <p> <code>COMMON</code> – Detects a variety of bots that identify themselves, such as web scraping frameworks, search engines, and automated browsers.</p> </li> <li> <p> <code>TARGETED</code> – Includes the <code>COMMON</code> protections, and adds detection for sophisticated bots that don't identify themselves. This level uses rate limiting, CAPTCHA, and background browser challenges.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WafBotControlConfig) -> dict:
    out: dict = {}
    if "inspection_level" in value:
        import capo_lightsail.types.waf_inspection_level_enum

        out["inspectionLevel"] = (
            capo_lightsail.types.waf_inspection_level_enum.serialize_aws_json_1_1(
                value["inspection_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WafBotControlConfig:
    out: WafBotControlConfig = {}  # type: ignore[typeddict-item]
    if data.get("inspectionLevel") is not None:
        import capo_lightsail.types.waf_inspection_level_enum

        out["inspection_level"] = (
            capo_lightsail.types.waf_inspection_level_enum.deserialize_aws_json_1_1(
                data["inspectionLevel"]
            )
        )
    return out
