/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
    // config.contentsCss = '/static/assets/css/custom_style.css'
    config.font_names = 'Montserrat Black/Montserrat Black; Montserrat Light/Montserrat Light; Monterchi Book/Monterchi Book; Bebas Neue Bold/Bebas Neue Bold;Mozer book/Mozer book' + config.font_names;
    config.image_prefillDimensions = false;
    config.disableObjectResizing=true;
    config.youtube_responsive = true;
};
