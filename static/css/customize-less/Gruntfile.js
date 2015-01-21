module.exports = function(grunt) {
	//do grunt-related things in here
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		less: {
			compileCore: {
				src: '<%= pkg.name%>.less',
				dest: '../customize/<%= pkg.name %>.css'
			}
		}
	});

	//加载包含less任务的插件
	grunt.loadNpmTasks('grunt-contrib-less');

	//默认被执行的任务列表
	grunt.registerTask('default', ['less']);
}