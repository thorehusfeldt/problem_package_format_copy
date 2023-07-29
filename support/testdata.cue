package problem_package

#testdata_settings: {
	input_validator_flags?: *"" | string | {[string]: string}
	output_validator_flags?: *"" | string
	grading?: {
		score?:               number
		max_score?:           number
		score_aggregation?:   "sum" | "min"
		verdict_aggregation?: "first_error" | "accept_if_any_accepted"
	}
}

#testdata_settings
