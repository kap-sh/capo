"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineSideOfStreetOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position
    import capo_geo_routes.types.side_of_street_matching_strategy


class IsolineSideOfStreetOptions(TypedDict, closed=True):
    position: "capo_geo_routes.types.position.Position"
    """<p>The <code>[longitude, latitude]</code> coordinates of the point that should be matched to a specific side of the street.</p>"""
    use_with: NotRequired[
        "capo_geo_routes.types.side_of_street_matching_strategy.SideOfStreetMatchingStrategy"
    ]
    """<p>Controls whether side-of-street matching is applied to any street (<code>AnyStreet</code>) or only to divided roads (<code>DividedStreetOnly</code>). This is important when the exact side of the street matters - for example, if a building entrance is only accessible from one side of a divided highway, or if a parking lot can only be entered from northbound lanes. Without correct side-of-street matching, travel time estimates may be inaccurate because they don't account for necessary U-turns or detours to reach the correct side.</p> <p>Default value: <code>DividedStreetOnly</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineSideOfStreetOptions) -> dict:
    out: dict = {}
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    if "use_with" in value:
        import capo_geo_routes.types.side_of_street_matching_strategy

        out["UseWith"] = (
            capo_geo_routes.types.side_of_street_matching_strategy.serialize_json(
                value["use_with"]
            )
        )
    return out


def deserialize_json(data: dict) -> IsolineSideOfStreetOptions:
    out: IsolineSideOfStreetOptions = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("IsolineSideOfStreetOptions.position required")
    if data.get("UseWith") is not None:
        import capo_geo_routes.types.side_of_street_matching_strategy

        out["use_with"] = (
            capo_geo_routes.types.side_of_street_matching_strategy.deserialize_json(
                data["UseWith"]
            )
        )
    return out


def redact_sensitive(value: IsolineSideOfStreetOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    return out
