"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalSite``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_probing_depth_millimeters
    import capo_connecthealth.types.periodontal_recession_millimeters
    import capo_connecthealth.types.periodontal_site_name


class PeriodontalSite(TypedDict, closed=True):
    site: "capo_connecthealth.types.periodontal_site_name.PeriodontalSiteName"
    """<p>The probing site. The following values are valid:</p> <ul> <li> <p> <code>DB</code>: Distobuccal.</p> </li> <li> <p> <code>B</code>: Buccal.</p> </li> <li> <p> <code>MB</code>: Mesiobuccal.</p> </li> <li> <p> <code>DL</code>: Distolingual.</p> </li> <li> <p> <code>L</code>: Lingual.</p> </li> <li> <p> <code>ML</code>: Mesiolingual.</p> </li> </ul>"""
    probing_depth: NotRequired[
        "capo_connecthealth.types.periodontal_probing_depth_millimeters.PeriodontalProbingDepthMillimeters"
    ]
    """<p>The probing depth, in millimeters. The value ranges from 0 to 15.</p>"""
    recession: NotRequired[
        "capo_connecthealth.types.periodontal_recession_millimeters.PeriodontalRecessionMillimeters"
    ]
    """<p>The gingival recession, in millimeters. The value ranges from -5 to 15. For example, <code>-1</code> represents "plus one."</p>"""
    bleeding: NotRequired["bool"]
    """<p>Specifies whether the site bled during probing.</p>"""
    suppuration: NotRequired["bool"]
    """<p>Specifies whether suppuration was present at the site.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalSite) -> dict:
    out: dict = {}
    import capo_connecthealth.types.periodontal_site_name

    out["site"] = capo_connecthealth.types.periodontal_site_name.serialize_json(
        value["site"]
    )
    if "probing_depth" in value:
        out["probingDepth"] = value["probing_depth"]
    if "recession" in value:
        out["recession"] = value["recession"]
    if "bleeding" in value:
        out["bleeding"] = value["bleeding"]
    if "suppuration" in value:
        out["suppuration"] = value["suppuration"]
    return out


def deserialize_json(data: dict) -> PeriodontalSite:
    out: PeriodontalSite = {}  # type: ignore[typeddict-item]
    if data.get("site") is not None:
        import capo_connecthealth.types.periodontal_site_name

        out["site"] = capo_connecthealth.types.periodontal_site_name.deserialize_json(
            data["site"]
        )
    else:
        import typing

        out["site"] = typing.cast(
            "capo_connecthealth.types.periodontal_site_name.PeriodontalSiteName", ""
        )
    if data.get("probingDepth") is not None:
        out["probing_depth"] = data["probingDepth"]
    if data.get("recession") is not None:
        out["recession"] = data["recession"]
    if data.get("bleeding") is not None:
        out["bleeding"] = data["bleeding"]
    if data.get("suppuration") is not None:
        out["suppuration"] = data["suppuration"]
    return out
