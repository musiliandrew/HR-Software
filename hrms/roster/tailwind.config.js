import frappeUIPreset from "frappe-ui/src/tailwind/preset";
import colors from "tailwindcss/colors";

export default {
	presets: [frappeUIPreset],
	content: [
		"./index.html",
		"./src/**/*.{vue,js,ts,jsx,tsx}",
		"./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
		"../node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
	],
	theme: {
		extend: {
			colors: {
				slate: colors.slate,
				zinc: colors.zinc,
				neutral: colors.neutral,
				indigo: colors.indigo,
				violet: colors.violet,
				purple: colors.purple,
				emerald: colors.emerald,
				rose: colors.rose,
				amber: colors.amber,
				cyan: colors.cyan,
				sky: colors.sky,
				teal: colors.teal,
			},
		},
	},
	plugins: [],
};
