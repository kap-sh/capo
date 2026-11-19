"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalTooth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_grade
    import capo_connecthealth.types.periodontal_site_list
    import capo_connecthealth.types.periodontal_tooth_number


class PeriodontalTooth(TypedDict, closed=True):
    tooth_number: (
        "capo_connecthealth.types.periodontal_tooth_number.PeriodontalToothNumber"
    )
    """<p>The tooth number in the Universal Numbering System. The value ranges from 1 to 32.</p>"""
    missing: "bool"
    """<p>Specifies whether the tooth is missing.</p>"""
    mobility: NotRequired["capo_connecthealth.types.periodontal_grade.PeriodontalGrade"]
    """<p>The tooth mobility grade. The value ranges from 0 to 3.</p>"""
    furcation: NotRequired[
        "capo_connecthealth.types.periodontal_grade.PeriodontalGrade"
    ]
    """<p>The furcation involvement class. The value ranges from 0 to 3.</p>"""
    sites: NotRequired[
        "capo_connecthealth.types.periodontal_site_list.PeriodontalSiteList"
    ]
    """<p>The probing sites that have a recorded measurement, in the order <code>MB</code>, <code>B</code>, <code>DB</code>, <code>ML</code>, <code>L</code>, <code>DL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalTooth) -> dict:
    out: dict = {}
    out["toothNumber"] = value["tooth_number"]
    out["missing"] = value["missing"]
    if "mobility" in value:
        out["mobility"] = value["mobility"]
    if "furcation" in value:
        out["furcation"] = value["furcation"]
    if "sites" in value:
        import capo_connecthealth.types.periodontal_site_list

        out["sites"] = capo_connecthealth.types.periodontal_site_list.serialize_json(
            value["sites"]
        )
    return out


def deserialize_json(data: dict) -> PeriodontalTooth:
    out: PeriodontalTooth = {}  # type: ignore[typeddict-item]
    if data.get("toothNumber") is not None:
        out["tooth_number"] = data["toothNumber"]
    else:
        out["tooth_number"] = 0
    if data.get("missing") is not None:
        out["missing"] = data["missing"]
    else:
        out["missing"] = False
    if data.get("mobility") is not None:
        out["mobility"] = data["mobility"]
    if data.get("furcation") is not None:
        out["furcation"] = data["furcation"]
    if data.get("sites") is not None:
        import capo_connecthealth.types.periodontal_site_list

        out["sites"] = capo_connecthealth.types.periodontal_site_list.deserialize_json(
            data["sites"]
        )
    return out
