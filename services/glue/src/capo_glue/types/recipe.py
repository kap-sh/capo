"""Generated from Smithy shape ``com.amazonaws.glue#Recipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.node_name
    import capo_glue.types.one_input
    import capo_glue.types.recipe_reference
    import capo_glue.types.recipe_steps


class Recipe(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Glue Studio node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the recipe node, identified by id.</p>"""
    recipe_reference: NotRequired["capo_glue.types.recipe_reference.RecipeReference"]
    """<p>A reference to the DataBrew recipe used by the node.</p>"""
    recipe_steps: NotRequired["capo_glue.types.recipe_steps.RecipeSteps"]
    """<p>Transform steps used in the recipe node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Recipe) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "recipe_reference" in value:
        import capo_glue.types.recipe_reference

        out["RecipeReference"] = (
            capo_glue.types.recipe_reference.serialize_aws_json_1_1(
                value["recipe_reference"]
            )
        )
    if "recipe_steps" in value:
        import capo_glue.types.recipe_steps

        out["RecipeSteps"] = capo_glue.types.recipe_steps.serialize_aws_json_1_1(
            value["recipe_steps"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Recipe:
    out: Recipe = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("RecipeReference") is not None:
        import capo_glue.types.recipe_reference

        out["recipe_reference"] = (
            capo_glue.types.recipe_reference.deserialize_aws_json_1_1(
                data["RecipeReference"]
            )
        )
    if data.get("RecipeSteps") is not None:
        import capo_glue.types.recipe_steps

        out["recipe_steps"] = capo_glue.types.recipe_steps.deserialize_aws_json_1_1(
            data["RecipeSteps"]
        )
    return out
