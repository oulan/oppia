from core.domain import widget_domain


class FileReadInput(widget_domain.BaseWidget):
    """Interactive widget for reading files."""

    # The human-readable name of the widget.
    name = 'File upload'

    # The category the widget falls under in the widget repository.
    category = 'Basic Input'

    # A description of the widget.
    description = 'A widget for uploading files.'

    # Customization args and their descriptions, schemas and default
    # values.
    _customization_arg_specs = []

    # Actions that the reader can perform on this widget which trigger a
    # feedback interaction, and the associated input types. Interactive widgets
    # must have at least one of these. This attribute name MUST be prefixed by
    # '_'.
    _handlers = [{
        'name': 'submit', 'obj_type': 'UnicodeString'
    }]

    # Additional JS library dependencies that should be loaded in pages
    # containing this widget. These should correspond to names of files in
    # feconf.DEPENDENCIES_TEMPLATES_DIR.
    _dependency_ids = []