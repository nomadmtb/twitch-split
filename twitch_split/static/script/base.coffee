$ ->
	checkfornotice()

checkfornotice = ->
	if $("#notice_wrapper").length
		$("#notice_wrapper").hide()
		setTimeout (->
			$("#notice_wrapper").slideToggle "fast"
			return
			), 2000

		setTimeout (->
			$("#notice_wrapper").slideToggle "fast"
			return
			), ($(".notice").length * 4500)