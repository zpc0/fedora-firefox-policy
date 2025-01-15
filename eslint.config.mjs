import json from "@eslint/json";
export default [
	{
		plugins: {
			json,
		},
	},
	{
		files: ["**/*.json"],
		language: "json/json",
		...json.configs.recommended,
	},
];
