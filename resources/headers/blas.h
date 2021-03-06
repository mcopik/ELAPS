#ifndef BLAS_H
#define BLAS_H
typedef struct {
    float r, i;
} floatc_t;
typedef struct {
    double r, i;
} doublec_t;
void srotg(float *, float *, float *, float *);
void drotg(double *, double *, double *, double *);
void srotmg(float *, float *, float *, float *, float *);
void drotmg(double *, double *, double *, double *, double *);
void srot(int *, float *, int *, float *, int *, float *, float *);
void drot(int *, double *, int *, double *, int *, double *, double *);
void srotm(int *, float *, int *, float *, int *, float *);
void drotm(int *, double *, int *, double *, int *, double *);
void sswap(int *, float *, int *, float *, int *);
void dswap(int *, double *, int *, double *, int *);
void cswap(int *, float *, int *, float *, int *);
void zswap(int *, double *, int *, double *, int *);
void sscal(int *, float *, float *, int *);
void dscal(int *, double *, double *, int *);
void cscal(int *, float *, float *, int *);
void zscal(int *, double *, double *, int *);
void csscal(int *, float *, float *, int *);
void zdscal(int *, double *, double *, int *);
void scopy(int *, float *, int *, float *, int *);
void dcopy(int *, double *, int *, double *, int *);
void ccopy(int *, float *, int *, float *, int *);
void zcopy(int *, double *, int *, double *, int *);
void saxpy(int *, float *, float *, int *, float *, int *);
void daxpy(int *, double *, double *, int *, double *, int *);
void caxpy(int *, float *, float *, int *, float *, int *);
void zaxpy(int *, double *, double *, int *, double *, int *);
float sdot(int *, float *, int *, float *, int *);
double ddot(int *, double *, int *, double *, int *);
double dsdot(int *, float *, int *, float *, int *);
floatc_t cdotu(int *, float *, int *, float *, int *);
doublec_t zdotu(int *, double *, int *, double *, int *);
floatc_t cdotc(int *, float *, int *, float *, int *);
doublec_t zdotc(int *, double *, int *, double *, int *);
float sdsdot(int *, float *, float *, int *, float *, int *);
float snrm2(int *, float *, int *);
double dnrm2(int *, double *, int *);
float scnrm2(int *, float *, int *);
double dznrm2(int *, double *, int *);
float sasum(int *, float *, int *);
double dasum(int *, double *, int *);
float scasum(int *, float *, int *);
double dzasum(int *, double *, int *);
int isamax(int *, float *, int *);
int idamax(int *, double *, int *);
int icamax(int *, float *, int *);
int izamax(int *, double *, int *);
void sgemv(char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dgemv(char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void cgemv(char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zgemv(char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void sgbmv(char *, int *, int *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dgbmv(char *, int *, int *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void cgbmv(char *, int *, int *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zgbmv(char *, int *, int *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void chemv(char *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zhemv(char *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void chbmv(char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zhbmv(char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void chpmv(char *, int *, float *, float *, float *, int *, float *, float *, int *);
void zhpmv(char *, int *, double *, double *, double *, int *, double *, double *, int *);
void ssymv(char *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dsymv(char *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void ssbmv(char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dsbmv(char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void sspmv(char *, int *, float *, float *, float *, int *, float *, float *, int *);
void dspmv(char *, int *, double *, double *, double *, int *, double *, double *, int *);
void strmv(char *, char *, char *, int *, float *, int *, float *, int *);
void dtrmv(char *, char *, char *, int *, double *, int *, double *, int *);
void ctrmv(char *, char *, char *, int *, float *, int *, float *, int *);
void ztrmv(char *, char *, char *, int *, double *, int *, double *, int *);
void stbmv(char *, char *, char *, int *, int *, float *, int *, float *, int *);
void dtbmv(char *, char *, char *, int *, int *, double *, int *, double *, int *);
void ctbmv(char *, char *, char *, int *, int *, float *, int *, float *, int *);
void ztbmv(char *, char *, char *, int *, int *, double *, int *, double *, int *);
void stpmv(char *, char *, char *, int *, float *, float *, int *);
void dtpmv(char *, char *, char *, int *, double *, double *, int *);
void ctpmv(char *, char *, char *, int *, float *, float *, int *);
void ztpmv(char *, char *, char *, int *, double *, double *, int *);
void strsv(char *, char *, char *, int *, float *, int *, float *, int *);
void dtrsv(char *, char *, char *, int *, double *, int *, double *, int *);
void ctrsv(char *, char *, char *, int *, float *, int *, float *, int *);
void ztrsv(char *, char *, char *, int *, double *, int *, double *, int *);
void stbsv(char *, char *, char *, int *, int *, float *, int *, float *, int *);
void dtbsv(char *, char *, char *, int *, int *, double *, int *, double *, int *);
void ctbsv(char *, char *, char *, int *, int *, float *, int *, float *, int *);
void ztbsv(char *, char *, char *, int *, int *, double *, int *, double *, int *);
void stpsv(char *, char *, char *, int *, float *, float *, int *);
void dtpsv(char *, char *, char *, int *, double *, double *, int *);
void ctpsv(char *, char *, char *, int *, float *, float *, int *);
void ztpsv(char *, char *, char *, int *, double *, double *, int *);
void sger(int *, int *, float *, float *, int *, float *, int *, float *, int *);
void dger(int *, int *, double *, double *, int *, double *, int *, double *, int *);
void cgeru(int *, int *, float *, float *, int *, float *, int *, float *, int *);
void zgeru(int *, int *, double *, double *, int *, double *, int *, double *, int *);
void cgerc(int *, int *, float *, float *, int *, float *, int *, float *, int *);
void zgerc(int *, int *, double *, double *, int *, double *, int *, double *, int *);
void cher(char *, int *, float *, float *, int *, float *, int *);
void zher(char *, int *, double *, double *, int *, double *, int *);
void chpr(char *, int *, float *, float *, int *, float *);
void zhpr(char *, int *, double *, double *, int *, double *);
void cher2(char *, int *, float *, float *, int *, float *, int *, float *, int *);
void zher2(char *, int *, double *, double *, int *, double *, int *, double *, int *);
void chpr2(char *, int *, float *, float *, int *, float *, int *, float *);
void zhpr2(char *, int *, double *, double *, int *, double *, int *, double *);
void ssyr(char *, int *, float *, float *, int *, float *, int *);
void dsyr(char *, int *, double *, double *, int *, double *, int *);
void sspr(char *, int *, float *, float *, int *, float *);
void dspr(char *, int *, double *, double *, int *, double *);
void ssyr2(char *, int *, float *, float *, int *, float *, int *, float *, int *);
void dsyr2(char *, int *, double *, double *, int *, double *, int *, double *, int *);
void sspr2(char *, int *, float *, float *, int *, float *, int *, float *);
void dspr2(char *, int *, double *, double *, int *, double *, int *, double *);
void sgemm(char *, char *, int *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dgemm(char *, char *, int *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void cgemm(char *, char *, int *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zgemm(char *, char *, int *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void ssymm(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dsymm(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void csymm(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zsymm(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void chemm(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zhemm(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void ssyrk(char *, char *, int *, int *, float *, float *, int *, float *, float *, int *);
void dsyrk(char *, char *, int *, int *, double *, double *, int *, double *, double *, int *);
void csyrk(char *, char *, int *, int *, float *, float *, int *, float *, float *, int *);
void zsyrk(char *, char *, int *, int *, double *, double *, int *, double *, double *, int *);
void cherk(char *, char *, int *, int *, float *, float *, int *, float *, float *, int *);
void zherk(char *, char *, int *, int *, double *, double *, int *, double *, double *, int *);
void ssyr2k(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void dsyr2k(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void csyr2k(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zsyr2k(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void cher2k(char *, char *, int *, int *, float *, float *, int *, float *, int *, float *, float *, int *);
void zher2k(char *, char *, int *, int *, double *, double *, int *, double *, int *, double *, double *, int *);
void strmm(char *, char *, char *, char *, int *, int *, float *, float *, int *, float *, int *);
void dtrmm(char *, char *, char *, char *, int *, int *, double *, double *, int *, double *, int *);
void ctrmm(char *, char *, char *, char *, int *, int *, float *, float *, int *, float *, int *);
void ztrmm(char *, char *, char *, char *, int *, int *, double *, double *, int *, double *, int *);
void strsm(char *, char *, char *, char *, int *, int *, float *, float *, int *, float *, int *);
void dtrsm(char *, char *, char *, char *, int *, int *, double *, double *, int *, double *, int *);
void ctrsm(char *, char *, char *, char *, int *, int *, float *, float *, int *, float *, int *);
void ztrsm(char *, char *, char *, char *, int *, int *, double *, double *, int *, double *, int *);
#endif /* BLAS_H */
