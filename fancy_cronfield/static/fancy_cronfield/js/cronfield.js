/*
 * jQuery plugin for Django Fancy Cronfield
 * https://github.com/saeedsq/django-fancy-cronfield
 *
 * Copyright (c) 2015, Saeed Salehian.
 * Licensed under BSD 3-clause "New" or "Revised" license.
 *
 * Requires:
 * - jQuery 1.4.1
 * - jQuery-cron
 * - jQuery-gentleSelect
 *
 * Usage:
 *  (JS)
 *
 *  // initialise like this
 *  var c = $('#cron').cron_field({
 *    initial: '9 10 * * *', # Initial value. default = "* * * * *"
 *    url_set: '/set/', # POST expecting {"cron": "12 10 * * 6"}
 *  });
 *
 *  // you can update values later
 *  c.cron("value", "1 2 3 4 *");
 *
 * // you can also get the current value using the "value" option
 * console.log(c.cron("value"));
 *
 *  (HTML)
 *  <div id='cron'></div>
 *
 * Notes:
 * At this stage, we only support a subset of possible cron options.
 * For example, each cron entry can only be digits or "*", no commas
 * to denote multiple entries. We also limit the allowed combinations:
 * - Every minute : * * * * *
 * - Every hour   : ? * * * *
 * - Every day    : ? ? * * *
 * - Every week   : ? ? * * ?
 * - Every month  : ? ? ? * *
 * - Every year   : ? ? ? ? *
 */
(function($) {
    window.cron_objs = {};

    $.fn.exists = function() {
        return this.length > 0;
    };

    $.fn.cron_field = function(options) {
        var cron_id = this.attr('id') + '-cron';
        if ($('#' + cron_id).exists()) {
            if (window.cron_objs[cron_id] !== undefined) {
                return window.cron_objs[cron_id];
            }
        }
        else {
            var cron_widget = $('<div>', {id: cron_id, 'class': 'cronfield'});
            this.before(cron_widget);
        }

        $('.field-' + this.attr('name')).removeClass('hidden');

        var input = this;
        var defaults = {
            initial: input.val() || '0 0 1 1 *',
            allowMultiple_all: true,
            allowMultiple_dom: true,
            allowMultiple_month: true,
            allowMultiple_dow: true,
            allowMultiple_hour: true,
            allowMultiple_minute: true,
            useGentleSelect: true,

            onChange: function() {
                input.val($(this).cron('value'));
            }
        };

        options = options ? options : {};
        options = $.extend({}, defaults, options);

        window.cron_objs[cron_id] = $('#' + cron_id).cron(options);
        return window.cron_objs[cron_id];
    };

    var options_mapping = {
        allowMultiple_all: 'data-allow_multiple_all',
        allowMultiple_dom: 'data-allow_multiple_dom',
        allowMultiple_month: 'data-allow_multiple_month',
        allowMultiple_dow: 'data-allow_multiple_dow',
        allowMultiple_hour: 'data-allow_multiple_minute',
        allowMultiple_minute: 'data-allow_multiple_minute',
        useGentleSelect: 'data-use_gentle_select'
    };
    $.fn.setup_cron_fields = function() {
        this.each(function() {
            var id = $(this).attr('id');
            if (id === undefined) {
                id = Math.floor((Math.random() * 1000000) + 1);
                $(this).attr('id', id);
            }
            if (id.indexOf('__prefix__') === -1) {
                var options = {};
                for (var key in options_mapping) {
                    if (options_mapping.hasOwnProperty(key)) {
                        var value = options_mapping[key];
                        options[key] = $(this).attr(value) !== undefined;
                        options[key] = options[key] && $(this).attr(value) !== '0';
                    }
                }
                $(this).cron_field(options);
            }
        });
    };

    $(document).ready(function($) {
        setTimeout(function() {
            $('input[data-fancy=cron]').setup_cron_fields();

            if ($('.empty-form input[data-fancy=cron]').exists()) {
                $('tr.add-row a').click(function() {
                    var parent = $(this).parents('table');
                    var items = parent.find('input[data-fancy=cron]');
                    items.setup_cron_fields();
                });
            }
        }, 500);
    });
})(jQuery_1_4_1);
