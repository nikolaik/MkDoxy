CONFIG = {
	"header": False,
	"breadcrumbs": True,
	"source": False,
	"start": 1,
	"end": 0,
}

TEMPLATE = """
{% if config.get('header') -%}
# {{node.kind.value|title}} {{node.name_long}}
{%- endif %}


{% if config.get('breadcrumbs') -%}
[**{{node.name_long if node.is_group else node.name_short}}**]({{node.url_source}})
{%- endif %}

{% if config.get('source') -%}
# [Go to the documentation of this file.]({{node.url}})
# {%- endif %}

{{code}}
"""
