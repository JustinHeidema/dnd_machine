/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 67);
/******/ })
/************************************************************************/
/******/ ({

/***/ 67:
/***/ (function(module, exports) {

throw new Error("Module build failed: SyntaxError: F:/Django/dnd_machine/dnd_machine/assets/js/index.js: JSX value should be either an expression or a quoted JSX text (305:44)\n\n\u001b[0m \u001b[90m 303 | \u001b[39m        \u001b[36mfor\u001b[39m (let i \u001b[33m=\u001b[39m \u001b[35m0\u001b[39m\u001b[33m;\u001b[39m i \u001b[33m<\u001b[39m \u001b[36mthis\u001b[39m\u001b[33m.\u001b[39mstate\u001b[33m.\u001b[39mrace_items\u001b[33m.\u001b[39mlanguages\u001b[33m.\u001b[39mlength\u001b[33m;\u001b[39m i\u001b[33m++\u001b[39m)\n \u001b[90m 304 | \u001b[39m        {\n\u001b[31m\u001b[1m>\u001b[22m\u001b[39m\u001b[90m 305 | \u001b[39m            language_array\u001b[33m.\u001b[39mpush(\u001b[33m<\u001b[39m\u001b[33minput\u001b[39m type\u001b[33m=\u001b[39mhidden value)\n \u001b[90m     | \u001b[39m                                            \u001b[31m\u001b[1m^\u001b[22m\u001b[39m\n \u001b[90m 306 | \u001b[39m        }\n \u001b[90m 307 | \u001b[39m    }\n \u001b[90m 308 | \u001b[39m\u001b[0m\n");

/***/ })

/******/ });