"""Generated from Smithy shape ``com.amazonaws.appmesh#SubjectAlternativeNameMatchers``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_app_mesh.types.subject_alternative_name_list


class SubjectAlternativeNameMatchers(TypedDict, closed=True):
    exact: (
        "capo_app_mesh.types.subject_alternative_name_list.SubjectAlternativeNameList"
    )
    """<p>The values sent must match the specified values exactly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubjectAlternativeNameMatchers) -> dict:
    out: dict = {}
    import capo_app_mesh.types.subject_alternative_name_list

    out["exact"] = capo_app_mesh.types.subject_alternative_name_list.serialize_json(
        value["exact"]
    )
    return out


def deserialize_json(data: dict) -> SubjectAlternativeNameMatchers:
    out: SubjectAlternativeNameMatchers = {}  # type: ignore[typeddict-item]
    if data.get("exact") is not None:
        import capo_app_mesh.types.subject_alternative_name_list

        out["exact"] = (
            capo_app_mesh.types.subject_alternative_name_list.deserialize_json(
                data["exact"]
            )
        )
    else:
        out["exact"] = []
    return out
